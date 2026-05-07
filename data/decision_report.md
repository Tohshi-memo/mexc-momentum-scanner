# Decision Report

- generated_at: 2026-05-07T04:06:36.524780+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3559**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3559, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.49% | **+0.46%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 7/20 | 35.0% | +0.53% | **+0.19%** |
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.46% | **+1.46%** |
| MARKET_LONG | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.30% | **+0.98%** |
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +1.08% | **+0.60%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$104.56** / 初期 $100.00 (+4.56%)
- 確定: 54件 (Win 18 / Loss 21 / Flat 15) / skip 66件
- 成長率目線: 平均log +0.000826 / 幾何平均 +0.083% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B3/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $104.56

## 4. Latest Market Context

- 更新: 2026-05-07T04:06:33.306618+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=80762.8
- Funnel: target 769 → liquid 186 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +228.91% | $1,491,168.05 |
| B3/USDT:USDT | +98.08% | $8,140,251.51 |
| DOGS/USDT:USDT | +73.38% | $10,133,724.89 |
| PENGUIN/USDT:USDT | +44.18% | $1,203,210.97 |
| FHE/USDT:USDT | +37.07% | $16,218,333.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +4.63% | +4.67% |
| FHE/USDT:USDT | below_1h_threshold | +2.78% | +2.82% |
| BILL/USDT:USDT | below_1h_threshold | +2.26% | +2.31% |
| NOT/USDT:USDT | below_1h_threshold | +1.92% | +1.96% |
| KSM/USDT:USDT | below_1h_threshold | +1.71% | +1.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
