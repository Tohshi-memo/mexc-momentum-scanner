# Decision Report

- generated_at: 2026-07-26T01:01:19.643399+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9552**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9552, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.77% | **-0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.49% | **+0.20%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.45% | **+1.84%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.86% | **+1.67%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.34% | **+0.93%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.64% | **+0.90%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$464.60** / 初期 $100.00 (+364.60%)
- 確定: 3380件 (Win 1075 / Loss 1096 / Flat 1209) / skip 2733件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EUL/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $464.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.34** / 初期 $100.00 (+39.34%)
- 確定: 1205件 (Win 335 / Loss 266 / Flat 604) / skip 1758件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1095 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $139.34

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.97** / 初期 $100.00 (+8.97%)
- 確定: 596件 (Win 203 / Loss 228 / Flat 165) / pending 1件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000511 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $108.97

## 6. Latest Market Context

- 更新: 2026-07-26T01:01:11.373101+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64496.4
- Funnel: target 898 → liquid 116 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +46.96% | $25,815,151.92 |
| ESPORTS/USDT:USDT | +19.97% | $28,426,740.79 |
| BANK/USDT:USDT | +19.48% | $86,110,342.06 |
| VELVET/USDT:USDT | +11.62% | $7,771,125.90 |
| ALLO/USDT:USDT | +10.52% | $18,947,859.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +0.44% | +0.42% |
| EVAA/USDT:USDT | below_1h_threshold | +0.37% | +0.35% |
| 1000BONK/USDT:USDT | below_1h_threshold | +0.36% | +0.33% |
| ONDO/USDT:USDT | below_1h_threshold | +0.29% | +0.27% |
| LAB/USDT:USDT | below_1h_threshold | +0.26% | +0.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
