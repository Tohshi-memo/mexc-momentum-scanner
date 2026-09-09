# Decision Report

- generated_at: 2026-09-09T06:01:18.300173+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14035**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.30% / filled 20/20。**
- 全期間 MARKET基準: n=14035, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.30% | **+1.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.64% | **+1.31%** |
| MARKET | 20/20 | 100.0% | +1.30% | **+1.30%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.72% | **+1.29%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.27% | **+1.20%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.85% | **+1.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.35% | **+0.21%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.70% | **-0.35%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,012.11** / 初期 $100.00 (+912.11%)
- 確定: 5299件 (Win 1591 / Loss 1708 / Flat 2000) / skip 5297件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,012.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.12** / 初期 $100.00 (+90.12%)
- 確定: 2638件 (Win 727 / Loss 623 / Flat 1288) / skip 4808件
- 成長率目線: 平均log +0.000244 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0086 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $190.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.43** / 初期 $100.00 (+18.43%)
- 確定: 2615件 (Win 764 / Loss 997 / Flat 854) / pending 5件 / skip 2887件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000213 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.43

## 6. Latest Market Context

- 更新: 2026-09-09T06:01:06.272324+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78931.8
- Funnel: target 1070 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +75.05% | $1,031,609.92 |
| OL/USDT:USDT | +23.70% | $2,127,372.95 |
| NIULAI/USDT:USDT | +17.27% | $1,302,862.89 |
| RAY/USDT:USDT | +16.88% | $2,957,441.53 |
| WAVES/USDT:USDT | +16.26% | $1,608,537.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +1.40% | +1.37% |
| CATE/USDT:USDT | below_1h_threshold | +0.98% | +0.95% |
| JUP/USDT:USDT | below_1h_threshold | +0.37% | +0.34% |
| LIT/USDT:USDT | below_1h_threshold | +0.35% | +0.31% |
| HYPE/USDT:USDT | below_1h_threshold | +0.23% | +0.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
