# Decision Report

- generated_at: 2026-07-18T00:46:23.691954+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8902**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=8902, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.31% | **+0.66%** |
| LIMIT_BB3S | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.73% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.77% | **+0.80%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.11% | **+0.67%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.58% | **+0.40%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$366.70** / 初期 $100.00 (+266.70%)
- 確定: 3017件 (Win 938 / Loss 959 / Flat 1120) / skip 2446件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $366.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.69** / 初期 $100.00 (+11.69%)
- 確定: 864件 (Win 203 / Loss 175 / Flat 486) / skip 1449件
- 成長率目線: 平均log +0.000128 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0727 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $111.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.54** / 初期 $100.00 (-0.46%)
- 確定: 160件 (Win 51 / Loss 86 / Flat 23) / pending 5件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000164 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $99.54

## 6. Latest Market Context

- 更新: 2026-07-18T00:46:12.997509+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=63896.9
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.0 >= 65=1, 4h RSI 75.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +54.70% | $10,677,356.44 |
| AKE/USDT:USDT | +16.60% | $49,163,037.03 |
| CASHCAT/USDT:USDT | +16.28% | $1,225,523.08 |
| BANK/USDT:USDT | +12.77% | $21,647,383.06 |
| CRO/USDT:USDT | +8.46% | $2,281,135.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PI/USDT:USDT | below_1h_threshold | +3.14% | +3.15% |
| PYTH/USDT:USDT | below_1h_threshold | +2.23% | +2.25% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +1.81% | +1.82% |
| DODO/USDT:USDT | below_1h_threshold | +1.56% | +1.57% |
| WIF/USDT:USDT | below_1h_threshold | +1.42% | +1.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
