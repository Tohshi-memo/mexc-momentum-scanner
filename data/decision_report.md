# Decision Report

- generated_at: 2026-05-11T18:12:52.552395+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4058**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4058, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.17% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.77% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.75% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.18% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 401件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T18:12:49.606529+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=81931.9
- Funnel: target 758 → liquid 192 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +13.91% | $2,534,460.36 |
| USELESS/USDT:USDT | +11.12% | $1,379,251.73 |
| PENGUIN/USDT:USDT | +9.70% | $2,194,513.17 |
| B/USDT:USDT | +6.88% | $28,803,356.30 |
| CRCLSTOCK/USDT:USDT | +5.62% | $8,081,937.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +3.67% | +3.63% |
| XNY/USDT:USDT | below_1h_threshold | +2.50% | +2.46% |
| VVV/USDT:USDT | below_1h_threshold | +2.15% | +2.10% |
| BASED/USDT:USDT | below_1h_threshold | +1.52% | +1.47% |
| BANANAS31/USDT:USDT | below_1h_threshold | +1.46% | +1.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
