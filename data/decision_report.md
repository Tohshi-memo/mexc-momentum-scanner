# Decision Report

- generated_at: 2026-09-13T00:41:15.314219+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14332**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.39% / filled 20/20。**
- 全期間 MARKET基準: n=14332, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_7PCT | 6/20 | 30.0% | +4.27% | **+1.28%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.03% | **+1.06%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.71% | **+0.64%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.91% | **+0.72%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.75% | **+0.71%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.76% | **+0.57%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.29% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5463件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$215.26** / 初期 $100.00 (+115.26%)
- 確定: 2850件 (Win 787 / Loss 661 / Flat 1402) / skip 4893件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1253 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $215.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.91** / 初期 $100.00 (+24.91%)
- 確定: 2783件 (Win 825 / Loss 1069 / Flat 889) / pending 5件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000473 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $124.91

## 6. Latest Market Context

- 更新: 2026-09-13T00:41:04.884929+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=77181.7
- Funnel: target 1068 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZCAT/USDT:USDT | +37.65% | $1,010,302.88 |
| LSK/USDT:USDT | +33.87% | $57,325,402.50 |
| STORJ/USDT:USDT | +21.90% | $20,537,162.09 |
| LONGXIA/USDT:USDT | +15.29% | $9,879,390.16 |
| ALCH/USDT:USDT | +15.01% | $2,451,217.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +4.57% | +4.65% |
| ZCAT/USDT:USDT | below_1h_threshold | +4.01% | +4.09% |
| INJ/USDT:USDT | below_1h_threshold | +1.59% | +1.67% |
| UAI/USDT:USDT | below_1h_threshold | +1.43% | +1.51% |
| ALCH/USDT:USDT | below_1h_threshold | +0.96% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
