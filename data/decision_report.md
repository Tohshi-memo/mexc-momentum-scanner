# Decision Report

- generated_at: 2026-07-12T10:01:17.274533+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8581**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8581, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 3/20 | 15.0% | +1.03% | **+0.15%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.02% | **+0.01%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.02% | **-0.00%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.77% | **-0.35%** |
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +2.82% | **+2.82%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.71% | **+1.11%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.06% | **+0.74%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.79% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$102.02** / 初期 $100.00 (+2.02%)
- 確定トレード: 87件 (TP 30 / SL 56 / EXP 1)
- 最新: VANRY/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$319.51** / 初期 $100.00 (+219.51%)
- 確定: 2769件 (Win 870 / Loss 921 / Flat 978) / skip 2373件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAC/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $319.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 644件 (Win 152 / Loss 159 / Flat 333) / skip 1348件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0394 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.17** / 初期 $100.00 (-0.83%)
- 確定: 26件 (Win 9 / Loss 17 / Flat 0) / pending 0件 / skip 27件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: T/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.17

## 6. Latest Market Context

- 更新: 2026-07-12T10:01:10.896740+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=63930.0
- Funnel: target 863 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SXT/USDT:USDT | +23.55% | $18,598,619.28 |
| B/USDT:USDT | +21.02% | $44,915,947.66 |
| VANRY/USDT:USDT | +17.67% | $3,022,515.08 |
| CLO/USDT:USDT | +15.85% | $1,144,925.29 |
| BILL/USDT:USDT | +14.59% | $2,300,148.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| METASTOCK/USDT:USDT | below_1h_threshold | +0.58% | +0.58% |
| SXT/USDT:USDT | below_1h_threshold | +0.51% | +0.51% |
| FHE/USDT:USDT | below_1h_threshold | +0.31% | +0.31% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.22% | +0.22% |
| XMR/USDT:USDT | below_1h_threshold | +0.17% | +0.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
