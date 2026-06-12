# Decision Report

- generated_at: 2026-06-12T17:00:28.592638+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6526**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.56% / filled 20/20。**
- 全期間 MARKET基準: n=6526, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.56% | **+0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.73% | **+0.44%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| ASK | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.87% | **+1.93%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.46% | **+0.80%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.92% | **+0.69%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.95% | **+0.62%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$94.22** / 初期 $100.00 (-5.78%)
- 確定トレード: 22件 (TP 3 / SL 18 / EXP 1)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $94.22
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$163.85** / 初期 $100.00 (+63.85%)
- 確定: 1399件 (Win 385 / Loss 457 / Flat 557) / skip 1688件
- 成長率目線: 平均log +0.000353 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $163.85

## 4. Latest Market Context

- 更新: 2026-06-12T17:00:19.111872+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.62% price=63950.0
- Funnel: target 774 → liquid 161 → pre 50 → checked 50 → surge 8 → strict 5
- Surge前reject: below_1h_threshold=41, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.9 >= 65=1, 4h RSI 80.1 >= 65=1, 4h RSI 74.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +17.56% | $6,369,622.17 |
| BTW/USDT:USDT | +9.64% | $2,933,585.58 |
| AIN/USDT:USDT | +9.27% | $1,524,491.45 |
| BEAT/USDT:USDT | +7.89% | $213,067,381.60 |
| RKLBSTOCK/USDT:USDT | +7.17% | $1,502,776.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COAI/USDT:USDT | below_relative_strength | +5.35% | +4.74% |
| SOXL/USDT:USDT | below_1h_threshold | +4.53% | +3.92% |
| ENJ/USDT:USDT | below_1h_threshold | +4.28% | +3.67% |
| PLSTOCK/USDT:USDT | below_1h_threshold | +3.99% | +3.38% |
| LIT/USDT:USDT | below_1h_threshold | +3.77% | +3.15% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
