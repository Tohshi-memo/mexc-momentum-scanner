# Decision Report

- generated_at: 2026-06-03T07:55:46.328831+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5529**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5529, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.80% | **-1.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.37% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.81% | **+1.40%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.45% | **+1.10%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.20% | **+0.54%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.71% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.89** / 初期 $100.00 (+30.89%)
- 確定: 983件 (Win 232 / Loss 303 / Flat 448) / skip 1107件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: WLD/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $130.89

## 4. Latest Market Context

- 更新: 2026-06-03T07:55:43.618225+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.46% price=67259.9
- Funnel: target 773 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +37.97% | $14,506,149.98 |
| AIA/USDT:USDT | +35.67% | $1,549,722.22 |
| GENIUS/USDT:USDT | +27.61% | $1,851,660.28 |
| CLO/USDT:USDT | +26.23% | $3,391,301.50 |
| APR/USDT:USDT | +24.58% | $1,333,522.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARKM/USDT:USDT | below_1h_threshold | +4.21% | +3.74% |
| US/USDT:USDT | below_1h_threshold | +4.12% | +3.66% |
| WLD/USDT:USDT | below_1h_threshold | +3.88% | +3.42% |
| SPX/USDT:USDT | below_1h_threshold | +2.28% | +1.81% |
| OP/USDT:USDT | below_1h_threshold | +2.27% | +1.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
