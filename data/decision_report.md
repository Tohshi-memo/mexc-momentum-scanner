# Decision Report

- generated_at: 2026-09-10T01:01:15.612814+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14136**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=14136, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.33% | **+1.19%** |
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.82% | **+1.00%** |
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.08% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.95% | **+1.56%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.44% | **+1.37%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.35% | **+0.28%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.81% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,019.63** / 初期 $100.00 (+919.63%)
- 確定: 5316件 (Win 1597 / Loss 1715 / Flat 2004) / skip 5381件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,019.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$202.22** / 初期 $100.00 (+102.22%)
- 確定: 2730件 (Win 753 / Loss 639 / Flat 1338) / skip 4817件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0720 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $202.22

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.58** / 初期 $100.00 (+20.58%)
- 確定: 2641件 (Win 777 / Loss 1009 / Flat 855) / pending 3件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000491 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $120.58

## 6. Latest Market Context

- 更新: 2026-09-10T01:01:07.314349+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78147.8
- Funnel: target 1064 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +21.31% | $2,794,771.70 |
| WAVES/USDT:USDT | +8.21% | $1,096,493.84 |
| SOCK/USDT:USDT | +8.13% | $1,089,021.37 |
| BTR/USDT:USDT | +5.98% | $2,179,941.08 |
| MINA/USDT:USDT | +4.81% | $1,239,545.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOCK/USDT:USDT | below_1h_threshold | +2.68% | +2.67% |
| BTR/USDT:USDT | below_1h_threshold | +2.19% | +2.18% |
| CATE/USDT:USDT | below_1h_threshold | +1.71% | +1.69% |
| SOXS/USDT:USDT | below_1h_threshold | +1.48% | +1.46% |
| MINA/USDT:USDT | below_1h_threshold | +0.45% | +0.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
