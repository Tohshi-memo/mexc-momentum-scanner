# Decision Report

- generated_at: 2026-07-18T02:46:33.035540+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8911**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.21% / filled 20/20。**
- 全期間 MARKET基準: n=8911, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.06% | **+1.03%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.77% | **+0.70%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.87% | **+0.65%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.72% | **+1.22%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.07% | **+0.64%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.53% | **+0.43%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.45% | **+0.39%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.55% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$362.35** / 初期 $100.00 (+262.35%)
- 確定: 3026件 (Win 939 / Loss 962 / Flat 1125) / skip 2446件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.43% 残高後 $362.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.66** / 初期 $100.00 (+11.66%)
- 確定: 873件 (Win 205 / Loss 177 / Flat 491) / skip 1449件
- 成長率目線: 平均log +0.000126 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0057 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $111.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.47** / 初期 $100.00 (-0.53%)
- 確定: 169件 (Win 53 / Loss 89 / Flat 27) / pending 5件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000190 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $99.47

## 6. Latest Market Context

- 更新: 2026-07-18T02:46:25.286066+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63938.7
- Funnel: target 885 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +57.51% | $11,996,963.24 |
| AKE/USDT:USDT | +28.28% | $48,225,039.82 |
| BANK/USDT:USDT | +15.71% | $22,462,964.11 |
| TRADOOR/USDT:USDT | +15.69% | $1,224,758.15 |
| VVV/USDT:USDT | +10.04% | $2,730,903.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +3.38% | +3.37% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.94% | +2.92% |
| TRADOOR/USDT:USDT | below_1h_threshold | +1.33% | +1.31% |
| SPX/USDT:USDT | below_1h_threshold | +1.09% | +1.08% |
| OP/USDT:USDT | below_1h_threshold | +1.04% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
