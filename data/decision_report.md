# Decision Report

- generated_at: 2026-09-03T22:11:13.531908+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13546**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13546, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.38% | **-1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_BB3S | 2/12 | 16.7% | +4.13% | **+0.69%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.69% | **+0.62%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.27% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +3.69% | **+2.63%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.74% | **+2.61%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.04% | **+2.13%** |
| MARKET_LONG | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.26% | **+1.13%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5099件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2373件 (Win 671 / Loss 576 / Flat 1126) / skip 4584件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0517 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.48** / 初期 $100.00 (+17.48%)
- 確定: 2213件 (Win 661 / Loss 867 / Flat 685) / pending 4件 / skip 2805件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000417 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PLTRSTOCK/USDT:USDT `MARKET_LONG` EXPIRED account -0.06% 残高後 $117.48

## 6. Latest Market Context

- 更新: 2026-09-03T22:11:06.882473+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=81387.7
- Funnel: target 1046 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +25.25% | $7,866,830.02 |
| BONER/USDT:USDT | +20.19% | $2,303,238.92 |
| AKE/USDT:USDT | +17.16% | $33,404,536.31 |
| BASECAT/USDT:USDT | +14.21% | $1,634,249.57 |
| APR/USDT:USDT | +10.89% | $2,582,786.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +1.87% | +2.07% |
| AKE/USDT:USDT | below_1h_threshold | +1.37% | +1.57% |
| BONER/USDT:USDT | below_1h_threshold | +1.22% | +1.41% |
| LIT/USDT:USDT | below_1h_threshold | +0.69% | +0.89% |
| FF/USDT:USDT | below_1h_threshold | +0.63% | +0.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
