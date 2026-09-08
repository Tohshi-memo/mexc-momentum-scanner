# Decision Report

- generated_at: 2026-09-08T12:36:18.380280+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13986**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.62% / filled 20/20。**
- 全期間 MARKET基準: n=13986, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.62% | **+1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.84% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | -0.60% | **-0.18%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.74% | **-0.45%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -2.28% | **-0.57%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,007.04** / 初期 $100.00 (+907.04%)
- 確定: 5250件 (Win 1584 / Loss 1707 / Flat 1959) / skip 5297件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,007.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.03** / 初期 $100.00 (+90.03%)
- 確定: 2589件 (Win 722 / Loss 622 / Flat 1245) / skip 4808件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0727 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $190.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.44** / 初期 $100.00 (+21.44%)
- 確定: 2575件 (Win 756 / Loss 969 / Flat 850) / pending 4件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000105 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $121.44

## 6. Latest Market Context

- 更新: 2026-09-08T12:36:08.430296+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=78363.0
- Funnel: target 1066 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +61.52% | $25,037,797.37 |
| BNCSTOCK/USDT:USDT | +26.34% | $1,951,660.99 |
| FORM/USDT:USDT | +20.21% | $4,387,923.83 |
| AKE/USDT:USDT | +17.59% | $10,611,036.89 |
| BONER/USDT:USDT | +17.42% | $2,990,771.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ATOM/USDT:USDT | below_1h_threshold | +3.66% | +3.70% |
| VVV/USDT:USDT | below_1h_threshold | +3.19% | +3.23% |
| CHIP/USDT:USDT | below_1h_threshold | +3.08% | +3.13% |
| ETC/USDT:USDT | below_1h_threshold | +1.54% | +1.59% |
| HNT/USDT:USDT | below_1h_threshold | +1.40% | +1.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
