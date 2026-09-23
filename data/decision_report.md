# Decision Report

- generated_at: 2026-09-23T08:16:24.067127+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15418**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15418, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.17% | **-0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.56% | **+0.90%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +3.05% | **+2.44%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.49% | **+1.87%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.46% | **+1.60%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.23% | **+0.98%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.68% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,222.05** / 初期 $100.00 (+1122.05%)
- 確定: 5890件 (Win 1739 / Loss 1886 / Flat 2265) / skip 6089件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SHROOM/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,222.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.11** / 初期 $100.00 (+149.11%)
- 確定: 3369件 (Win 930 / Loss 787 / Flat 1652) / skip 5460件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0382 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SHROOM/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.98** / 初期 $100.00 (+20.98%)
- 確定: 3133件 (Win 921 / Loss 1233 / Flat 979) / pending 3件 / skip 3758件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000178 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $120.98

## 6. Latest Market Context

- 更新: 2026-09-23T08:16:13.219882+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=86221.2
- Funnel: target 1061 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAKE/USDT:USDT | +156.50% | $2,175,356.04 |
| SHROOM/USDT:USDT | +66.94% | $1,325,650.05 |
| LONGXIA/USDT:USDT | +26.26% | $1,911,653.30 |
| SAGA/USDT:USDT | +21.69% | $1,723,063.18 |
| ALLO/USDT:USDT | +21.58% | $2,789,531.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +2.24% | +2.10% |
| ALLO/USDT:USDT | below_1h_threshold | +1.44% | +1.30% |
| BCH/USDT:USDT | below_1h_threshold | +1.27% | +1.13% |
| ZRO/USDT:USDT | below_1h_threshold | +1.26% | +1.12% |
| GRASS/USDT:USDT | below_1h_threshold | +0.98% | +0.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
