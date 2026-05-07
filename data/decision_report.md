# Decision Report

- generated_at: 2026-05-07T04:03:00.972885+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3558**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3558, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.28% | **+0.28%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 7/20 | 35.0% | +0.53% | **+0.19%** |
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.06% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.83% | **+1.83%** |
| MARKET_LONG | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.68% | **+1.18%** |
| LIMIT_BB3S_LONG | 5/10 | 50.0% | +1.08% | **+0.54%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$105.08** / 初期 $100.00 (+5.08%)
- 確定: 53件 (Win 18 / Loss 20 / Flat 15) / skip 66件
- 成長率目線: 平均log +0.000936 / 幾何平均 +0.094% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $105.08

## 4. Latest Market Context

- 更新: 2026-05-07T04:02:57.702476+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=80821.5
- Funnel: target 769 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +251.32% | $1,474,657.92 |
| B3/USDT:USDT | +140.12% | $8,037,479.20 |
| DOGS/USDT:USDT | +66.74% | $10,004,123.38 |
| PENGUIN/USDT:USDT | +37.93% | $1,198,008.60 |
| FHE/USDT:USDT | +35.72% | $16,190,740.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +1.61% | +1.58% |
| PENGUIN/USDT:USDT | below_1h_threshold | +1.45% | +1.42% |
| PLAY/USDT:USDT | below_1h_threshold | +1.10% | +1.07% |
| VVV/USDT:USDT | below_1h_threshold | +0.61% | +0.58% |
| ICP/USDT:USDT | below_1h_threshold | +0.51% | +0.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
