# Decision Report

- generated_at: 2026-08-05T04:31:43.101774+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10353**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10353, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/18 | 27.8% | +1.60% | **+0.44%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.64% | **+1.98%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.61% | **+1.44%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +3.46% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$600.80** / 初期 $100.00 (+500.80%)
- 確定: 3750件 (Win 1188 / Loss 1226 / Flat 1336) / skip 3164件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HFT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $600.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.04** / 初期 $100.00 (+40.04%)
- 確定: 1290件 (Win 361 / Loss 301 / Flat 628) / skip 2474件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0343 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $140.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.61** / 初期 $100.00 (+18.61%)
- 確定: 1109件 (Win 357 / Loss 427 / Flat 325) / pending 6件 / skip 717件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000288 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.61

## 6. Latest Market Context

- 更新: 2026-08-05T04:31:27.980627+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64126.1
- Funnel: target 939 → liquid 182 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.2 >= 65=1, 4h RSI 74.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +83.81% | $9,631,467.80 |
| BLESS/USDT:USDT | +38.01% | $22,537,760.55 |
| CASHCAT/USDT:USDT | +35.27% | $1,195,752.50 |
| TAKE/USDT:USDT | +35.06% | $1,571,629.24 |
| MARSCOIN/USDT:USDT | +31.69% | $1,157,277.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.84% | +3.87% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.86% | +2.89% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.85% | +2.88% |
| MVLL/USDT:USDT | below_1h_threshold | +2.82% | +2.85% |
| CASHCAT/USDT:USDT | below_1h_threshold | +2.43% | +2.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
