# Decision Report

- generated_at: 2026-07-20T15:01:11.153545+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9119**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9119, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.50% | **+1.27%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.58% | **+1.16%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +1.76% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$404.96** / 初期 $100.00 (+304.96%)
- 確定: 3181件 (Win 994 / Loss 1009 / Flat 1178) / skip 2499件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $404.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.25** / 初期 $100.00 (+27.25%)
- 確定: 1080件 (Win 281 / Loss 219 / Flat 580) / skip 1450件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0907 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: B/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $127.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.67** / 初期 $100.00 (+1.67%)
- 確定: 318件 (Win 110 / Loss 139 / Flat 69) / pending 4件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000298 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.67

## 6. Latest Market Context

- 更新: 2026-07-20T15:01:04.139680+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64411.9
- Funnel: target 885 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +90.42% | $28,111,481.85 |
| PROM/USDT:USDT | +74.64% | $8,102,235.46 |
| BANK/USDT:USDT | +73.71% | $121,584,964.92 |
| EVAA/USDT:USDT | +25.77% | $8,205,409.69 |
| PUMPFUN/USDT:USDT | +17.78% | $39,237,912.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.69% | +2.65% |
| B/USDT:USDT | below_1h_threshold | +1.31% | +1.28% |
| METASTOCK/USDT:USDT | below_1h_threshold | +1.23% | +1.19% |
| MVLL/USDT:USDT | below_1h_threshold | +1.19% | +1.16% |
| EVAA/USDT:USDT | below_1h_threshold | +1.09% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
