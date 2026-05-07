# Decision Report

- generated_at: 2026-05-07T08:07:46.592100+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3596**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3596, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +5.43% | **+1.63%** |
| LIMIT_8PCT | 7/20 | 35.0% | +3.83% | **+1.34%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.86% | **+0.30%** |
| LIMIT_BB3S | 10/18 | 55.6% | +0.31% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.05% | **+1.53%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.31** / 初期 $100.00 (+6.31%)
- 確定: 90件 (Win 31 / Loss 36 / Flat 23) / skip 67件
- 成長率目線: 平均log +0.000680 / 幾何平均 +0.068% per trade / maxDD +2.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: D/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $106.31

## 4. Latest Market Context

- 更新: 2026-05-07T08:07:43.526066+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=81522.6
- Funnel: target 771 → liquid 189 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +208.74% | $1,969,151.82 |
| PENGUIN/USDT:USDT | +125.84% | $2,078,099.64 |
| B3/USDT:USDT | +77.52% | $10,224,580.23 |
| DOGS/USDT:USDT | +69.35% | $12,972,563.50 |
| D/USDT:USDT | +61.79% | $1,061,926.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +2.34% | +2.28% |
| IO/USDT:USDT | below_1h_threshold | +1.96% | +1.91% |
| FHE/USDT:USDT | below_1h_threshold | +1.39% | +1.34% |
| NIL/USDT:USDT | below_1h_threshold | +1.31% | +1.26% |
| LAB/USDT:USDT | below_1h_threshold | +1.00% | +0.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
