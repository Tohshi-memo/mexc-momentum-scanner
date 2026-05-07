# Decision Report

- generated_at: 2026-05-07T09:37:35.974886+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3607**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3607, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_BB3S | 7/13 | 53.8% | +0.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.84% | **+1.73%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +3.93% | **+0.98%** |
| MARKET_LONG | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.06% | **+0.69%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.39% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.01** / 初期 $100.00 (+6.01%)
- 確定: 101件 (Win 34 / Loss 42 / Flat 25) / skip 67件
- 成長率目線: 平均log +0.000578 / 幾何平均 +0.058% per trade / maxDD +2.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $106.01

## 4. Latest Market Context

- 更新: 2026-05-07T09:37:32.867084+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=80989.6
- Funnel: target 771 → liquid 186 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +169.26% | $2,088,500.25 |
| PENGUIN/USDT:USDT | +116.67% | $2,861,968.41 |
| B3/USDT:USDT | +89.87% | $10,597,650.37 |
| DOGS/USDT:USDT | +61.38% | $14,297,607.69 |
| D/USDT:USDT | +51.24% | $1,178,465.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.69% | +4.94% |
| EVAA/USDT:USDT | below_1h_threshold | +3.82% | +4.08% |
| B3/USDT:USDT | below_1h_threshold | +3.06% | +3.31% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.41% | +2.66% |
| D/USDT:USDT | below_1h_threshold | +2.33% | +2.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
