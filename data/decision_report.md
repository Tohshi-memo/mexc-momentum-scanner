# Decision Report

- generated_at: 2026-07-19T14:01:15.122555+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9042**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9042, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.27% | **+1.02%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.97% | **+0.89%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.76% | **+0.72%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.58% | **+1.55%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.49% | **+0.75%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$401.36** / 初期 $100.00 (+301.36%)
- 確定: 3104件 (Win 973 / Loss 989 / Flat 1142) / skip 2499件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $401.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.42** / 初期 $100.00 (+27.42%)
- 確定: 1003件 (Win 259 / Loss 209 / Flat 535) / skip 1450件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1135 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $127.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.86** / 初期 $100.00 (+0.86%)
- 確定: 243件 (Win 82 / Loss 121 / Flat 40) / pending 1件 / skip 266件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000340 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $100.86

## 6. Latest Market Context

- 更新: 2026-07-19T14:01:05.829050+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=64452.9
- Funnel: target 885 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +139.58% | $39,961,811.23 |
| TLM/USDT:USDT | +74.16% | $8,409,913.48 |
| B/USDT:USDT | +43.81% | $31,326,147.10 |
| TAG/USDT:USDT | +26.85% | $4,742,108.54 |
| ESPORTS/USDT:USDT | +26.30% | $58,768,501.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.09% | +3.09% |
| TLM/USDT:USDT | below_1h_threshold | +1.50% | +1.50% |
| BULLA/USDT:USDT | below_1h_threshold | +1.04% | +1.04% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.63% | +0.63% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.50% | +0.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
