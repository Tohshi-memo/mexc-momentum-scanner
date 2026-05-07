# Decision Report

- generated_at: 2026-05-07T08:47:36.708904+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3601**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3601, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +3.85% | **+1.16%** |
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.67% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.06% | **+1.53%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.71% | **+1.36%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.08% | **+1.25%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.73% | **+1.09%** |
| MARKET_LONG | 20/20 | 100.0% | +1.04% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.01** / 初期 $100.00 (+6.01%)
- 確定: 95件 (Win 32 / Loss 39 / Flat 24) / skip 67件
- 成長率目線: 平均log +0.000614 / 幾何平均 +0.061% per trade / maxDD +2.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.00% 残高後 $106.01

## 4. Latest Market Context

- 更新: 2026-05-07T08:47:33.624505+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=81187.6
- Funnel: target 770 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +204.39% | $2,030,027.78 |
| PENGUIN/USDT:USDT | +99.50% | $2,476,241.71 |
| B3/USDT:USDT | +87.11% | $10,454,491.90 |
| DOGS/USDT:USDT | +63.97% | $13,940,208.00 |
| D/USDT:USDT | +48.23% | $1,143,614.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +4.50% | +4.86% |
| SATO/USDT:USDT | below_1h_threshold | +4.20% | +4.56% |
| WLFI/USDT:USDT | below_1h_threshold | +3.09% | +3.45% |
| B3/USDT:USDT | below_1h_threshold | +2.46% | +2.82% |
| ONDO/USDT:USDT | below_1h_threshold | +1.76% | +2.12% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
