# Decision Report

- generated_at: 2026-07-31T23:01:28.864167+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10034**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10034, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_BB3S | 6/20 | 30.0% | +2.08% | **+0.62%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.32% | **+2.33%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.64% | **+2.12%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.42% | **+1.35%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.86% | **+1.29%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.69% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$567.45** / 初期 $100.00 (+467.45%)
- 確定: 3586件 (Win 1147 / Loss 1170 / Flat 1269) / skip 3009件
- 成長率目線: 平均log +0.000484 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $567.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2166件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1009 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.18** / 初期 $100.00 (+12.18%)
- 確定: 859件 (Win 279 / Loss 338 / Flat 242) / pending 5件 / skip 647件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000346 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $112.18

## 6. Latest Market Context

- 更新: 2026-07-31T23:01:19.042052+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=62926.3
- Funnel: target 921 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +31.11% | $16,549,280.57 |
| JIMOTHY/USDT:USDT | +25.80% | $1,114,651.58 |
| TLM/USDT:USDT | +17.57% | $1,359,808.48 |
| FLOW/USDT:USDT | +15.92% | $1,212,573.10 |
| GIGGLE/USDT:USDT | +15.70% | $19,014,922.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +0.45% | +0.44% |
| 1000RATS/USDT:USDT | below_1h_threshold | +0.39% | +0.37% |
| ORDI/USDT:USDT | below_1h_threshold | +0.33% | +0.32% |
| MMT/USDT:USDT | below_1h_threshold | +0.29% | +0.28% |
| 1000BONK/USDT:USDT | below_1h_threshold | +0.25% | +0.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
