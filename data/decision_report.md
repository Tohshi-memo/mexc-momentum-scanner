# Decision Report

- generated_at: 2026-05-11T18:53:05.841208+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4062**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4062, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.46% | **+0.16%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.17% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.55% | **+1.40%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.30% | **+0.84%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.77% | **+0.83%** |
| ASK_LONG | 20/20 | 100.0% | +0.77% | **+0.77%** |
| MARKET_LONG | 20/20 | 100.0% | +0.63% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 405件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T18:52:56.653433+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=81978.2
- Funnel: target 758 → liquid 194 → pre 50 → checked 50 → surge 7 → strict 2
- Surge前reject: below_1h_threshold=42, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.2 >= 65=1, 4h RSI 86.8 >= 65=1, 4h RSI 78.9 >= 65=1, 4h RSI 79.2 >= 65=1, 4h RSI 72.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +19.14% | $114,608,112.82 |
| SKYAI/USDT:USDT | +18.06% | $31,398,912.97 |
| USELESS/USDT:USDT | +15.22% | $1,732,625.06 |
| SAGA/USDT:USDT | +14.76% | $5,464,454.91 |
| B/USDT:USDT | +13.70% | $31,225,151.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_relative_strength | +5.03% | +4.93% |
| BASED/USDT:USDT | below_1h_threshold | +4.76% | +4.66% |
| VVV/USDT:USDT | below_1h_threshold | +3.85% | +3.75% |
| NIGHT/USDT:USDT | below_1h_threshold | +2.54% | +2.44% |
| FHE/USDT:USDT | below_1h_threshold | +1.83% | +1.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
