# Decision Report

- generated_at: 2026-08-05T04:06:29.167321+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10350**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10350, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-3.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.40% | **-3.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_BB3S | 4/18 | 22.2% | +1.69% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.20% | **+3.20%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +4.04% | **+3.03%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +4.29% | **+2.14%** |
| LIMIT_ATR_LONG | 6/20 | 30.0% | +3.17% | **+0.95%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.92% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.85** / 初期 $100.00 (+506.85%)
- 確定: 3747件 (Win 1188 / Loss 1224 / Flat 1335) / skip 3164件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $606.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.02** / 初期 $100.00 (+41.02%)
- 確定: 1287件 (Win 361 / Loss 299 / Flat 627) / skip 2474件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0659 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $141.02

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.02** / 初期 $100.00 (+19.02%)
- 確定: 1106件 (Win 357 / Loss 425 / Flat 324) / pending 4件 / skip 716件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000309 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.02

## 6. Latest Market Context

- 更新: 2026-08-05T04:06:20.948503+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64115.4
- Funnel: target 939 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +83.91% | $9,033,294.96 |
| TAKE/USDT:USDT | +36.61% | $1,537,214.10 |
| BLESS/USDT:USDT | +31.29% | $21,424,744.44 |
| CASHCAT/USDT:USDT | +30.59% | $1,171,415.15 |
| MARSCOIN/USDT:USDT | +29.11% | $1,145,277.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.34% | +3.39% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.86% | +2.91% |
| MVLL/USDT:USDT | below_1h_threshold | +2.82% | +2.87% |
| BLESS/USDT:USDT | below_1h_threshold | +2.41% | +2.46% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +1.98% | +2.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
