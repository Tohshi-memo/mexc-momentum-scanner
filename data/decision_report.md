# Decision Report

- generated_at: 2026-09-23T08:31:27.375387+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15419**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=15419, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_5PCT | 6/20 | 30.0% | +3.65% | **+1.10%** |
| LIMIT_6PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.30% | **+1.84%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.69% | **+1.27%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.28% | **+0.77%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,215.94** / 初期 $100.00 (+1115.94%)
- 確定: 5891件 (Win 1739 / Loss 1887 / Flat 2265) / skip 6089件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,215.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.11** / 初期 $100.00 (+149.11%)
- 確定: 3370件 (Win 930 / Loss 787 / Flat 1653) / skip 5460件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0382 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $249.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.98** / 初期 $100.00 (+20.98%)
- 確定: 3133件 (Win 921 / Loss 1233 / Flat 979) / pending 3件 / skip 3758件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000178 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $120.98

## 6. Latest Market Context

- 更新: 2026-09-23T08:31:14.430172+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=86148.0
- Funnel: target 1061 → liquid 192 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAKE/USDT:USDT | +178.70% | $2,389,536.43 |
| SHROOM/USDT:USDT | +67.18% | $1,333,068.01 |
| LONGXIA/USDT:USDT | +26.78% | $1,936,453.63 |
| MET/USDT:USDT | +24.03% | $1,010,897.95 |
| ALLO/USDT:USDT | +22.64% | $2,865,579.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.79% | +3.73% |
| BCH/USDT:USDT | below_1h_threshold | +3.44% | +3.38% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.90% | +2.85% |
| TIA/USDT:USDT | below_1h_threshold | +2.34% | +2.28% |
| ALLO/USDT:USDT | below_1h_threshold | +2.23% | +2.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
