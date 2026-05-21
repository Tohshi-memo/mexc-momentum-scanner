# Decision Report

- generated_at: 2026-05-21T15:09:08.980763+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4642**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4642, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-1.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.41% | **-1.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +0.89% | **+0.71%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.54% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.42% | **+1.33%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.99% | **+1.20%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.49% | **+1.12%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.18% | **+0.98%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 657件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T15:09:06.619133+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=76870.1
- Funnel: target 766 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +56.57% | $15,102,107.72 |
| ROAM/USDT:USDT | +53.68% | $2,381,638.56 |
| NEX/USDT:USDT | +52.05% | $1,659,057.19 |
| EDEN/USDT:USDT | +49.49% | $33,970,459.44 |
| PROVE/USDT:USDT | +42.27% | $6,872,134.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROAM/USDT:USDT | below_1h_threshold | +3.76% | +3.86% |
| BEAT/USDT:USDT | below_1h_threshold | +2.78% | +2.87% |
| LIT/USDT:USDT | below_1h_threshold | +2.10% | +2.20% |
| HYPE/USDT:USDT | below_1h_threshold | +1.51% | +1.60% |
| BSB/USDT:USDT | below_1h_threshold | +1.37% | +1.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
