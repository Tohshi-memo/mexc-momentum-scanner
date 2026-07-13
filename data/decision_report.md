# Decision Report

- generated_at: 2026-07-13T09:11:12.755506+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8627**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=8627, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.29% | **+2.06%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.01% | **+1.61%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.06% | **+0.69%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.49% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +0.53% | **+0.45%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.33% | **-0.07%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.73% | **-0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -4.00% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.20** / 初期 $100.00 (+1.20%)
- 確定トレード: 91件 (TP 30 / SL 59 / EXP 2)
- 最新: ANSEM/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.39** / 初期 $100.00 (+221.39%)
- 確定: 2796件 (Win 876 / Loss 923 / Flat 997) / skip 2392件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $321.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 645件 (Win 152 / Loss 159 / Flat 334) / skip 1393件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0627 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.19** / 初期 $100.00 (+0.19%)
- 確定: 32件 (Win 13 / Loss 19 / Flat 0) / pending 3件 / skip 62件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000685 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $100.19

## 6. Latest Market Context

- 更新: 2026-07-13T09:11:06.524419+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=63118.4
- Funnel: target 863 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +26.93% | $1,177,797.96 |
| XEC/USDT:USDT | +26.51% | $4,443,645.27 |
| DODO/USDT:USDT | +20.30% | $7,286,180.81 |
| KITE/USDT:USDT | +19.67% | $2,200,135.02 |
| BLAST/USDT:USDT | +7.75% | $2,827,504.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +2.51% | +2.60% |
| BILL/USDT:USDT | below_1h_threshold | +2.34% | +2.43% |
| SYN/USDT:USDT | below_1h_threshold | +2.15% | +2.24% |
| TWLOSTOCK/USDT:USDT | below_1h_threshold | +1.67% | +1.76% |
| OGN/USDT:USDT | below_1h_threshold | +1.28% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
