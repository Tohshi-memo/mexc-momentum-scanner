# Decision Report

- generated_at: 2026-08-01T01:06:33.899338+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10040**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10040, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.43% | **+0.39%** |
| LIMIT_BB3S | 4/20 | 20.0% | +1.52% | **+0.30%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.49% | **+1.04%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.05% | **+0.84%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.77% | **+0.73%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.06% | **+0.58%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.37% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$572.59** / 初期 $100.00 (+472.59%)
- 確定: 3592件 (Win 1149 / Loss 1174 / Flat 1269) / skip 3009件
- 成長率目線: 平均log +0.000486 / 幾何平均 +0.049% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.05% 残高後 $572.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2172件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0255 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.97** / 初期 $100.00 (+11.97%)
- 確定: 863件 (Win 280 / Loss 341 / Flat 242) / pending 5件 / skip 648件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000286 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $111.97

## 6. Latest Market Context

- 更新: 2026-08-01T01:06:25.424992+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=62929.0
- Funnel: target 921 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +22.98% | $1,127,847.07 |
| GIGGLE/USDT:USDT | +19.57% | $21,771,296.81 |
| KOMA/USDT:USDT | +19.19% | $17,746,139.40 |
| 1000RATS/USDT:USDT | +17.26% | $17,520,899.07 |
| BTW/USDT:USDT | +16.89% | $1,853,517.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +2.19% | +2.16% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.63% | +1.60% |
| BTW/USDT:USDT | below_1h_threshold | +1.58% | +1.55% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.17% | +1.14% |
| ZAMA/USDT:USDT | below_1h_threshold | +0.97% | +0.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
