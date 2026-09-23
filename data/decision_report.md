# Decision Report

- generated_at: 2026-09-23T08:51:22.310736+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15421**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.89% / filled 20/20。**
- 全期間 MARKET基準: n=15421, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.89% | **+0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/11 | 45.5% | +4.00% | **+1.82%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.70% | **+1.19%** |
| LIMIT_5PCT | 5/20 | 25.0% | +4.19% | **+1.05%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.51% | **+0.91%** |
| MARKET | 20/20 | 100.0% | +0.89% | **+0.89%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.60% | **+1.28%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.38% | **+1.10%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.24% | **+0.87%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.24% | **+0.81%** |
| LIMIT_BB3S_LONG | 3/9 | 33.3% | +0.29% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,215.94** / 初期 $100.00 (+1115.94%)
- 確定: 5892件 (Win 1739 / Loss 1887 / Flat 2266) / skip 6090件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSV/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,215.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.11** / 初期 $100.00 (+149.11%)
- 確定: 3370件 (Win 930 / Loss 787 / Flat 1653) / skip 5462件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0382 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $249.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.32** / 初期 $100.00 (+21.32%)
- 確定: 3134件 (Win 922 / Loss 1233 / Flat 979) / pending 2件 / skip 3759件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000134 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BSV/USDT:USDT `MARKET` EXPIRED account +0.28% 残高後 $121.32

## 6. Latest Market Context

- 更新: 2026-09-23T08:51:12.335238+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=85766.3
- Funnel: target 1061 → liquid 192 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAKE/USDT:USDT | +201.98% | $2,777,405.44 |
| SHROOM/USDT:USDT | +66.52% | $1,339,661.42 |
| LONGXIA/USDT:USDT | +26.84% | $1,951,889.56 |
| MET/USDT:USDT | +24.81% | $1,034,276.15 |
| ALLO/USDT:USDT | +21.16% | $2,999,989.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_1h_threshold | +4.40% | +4.79% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.71% | +3.10% |
| BCH/USDT:USDT | below_1h_threshold | +2.00% | +2.38% |
| BLESS/USDT:USDT | below_1h_threshold | +1.91% | +2.30% |
| BR/USDT:USDT | below_1h_threshold | +1.41% | +1.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
