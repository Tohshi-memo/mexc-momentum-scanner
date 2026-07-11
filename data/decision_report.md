# Decision Report

- generated_at: 2026-07-11T22:26:06.591996+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8553**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8553, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.48% | **-0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +5.55% | **+1.39%** |
| LIMIT_BB3S | 2/16 | 12.5% | +6.15% | **+0.77%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.28% | **+1.82%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.86% | **+1.67%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$103.05** / 初期 $100.00 (+3.05%)
- 確定トレード: 85件 (TP 30 / SL 54 / EXP 1)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$322.68** / 初期 $100.00 (+222.68%)
- 確定: 2741件 (Win 866 / Loss 918 / Flat 957) / skip 2373件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $322.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 643件 (Win 152 / Loss 159 / Flat 332) / skip 1321件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0456 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.22** / 初期 $100.00 (+0.22%)
- 確定: 20件 (Win 9 / Loss 11 / Flat 0) / pending 1件 / skip 1件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000173 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.22

## 6. Latest Market Context

- 更新: 2026-07-11T22:25:59.486379+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=64271.3
- Funnel: target 863 → liquid 143 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SXT/USDT:USDT | +22.86% | $10,014,013.43 |
| CASHCAT/USDT:USDT | +12.88% | $1,865,831.36 |
| EVAA/USDT:USDT | +11.28% | $26,081,318.45 |
| TAC/USDT:USDT | +10.02% | $2,710,821.08 |
| CLO/USDT:USDT | +6.76% | $1,446,361.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +0.98% | +1.06% |
| VANRY/USDT:USDT | below_1h_threshold | +0.37% | +0.45% |
| VELVET/USDT:USDT | below_1h_threshold | +0.20% | +0.28% |
| SOXL/USDT:USDT | below_1h_threshold | +0.18% | +0.27% |
| COPSTOCK/USDT:USDT | below_1h_threshold | +0.13% | +0.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
