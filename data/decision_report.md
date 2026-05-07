# Decision Report

- generated_at: 2026-05-07T04:27:41.058346+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3564**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3564, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.77% | **-0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.08% | **+0.08%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.06% | **+0.01%** |
| ASK | 20/20 | 100.0% | -0.02% | **-0.02%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.11% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.00% | **+1.60%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +2.36% | **+1.57%** |
| ASK_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.55% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.55** / 初期 $100.00 (+6.55%)
- 確定: 58件 (Win 21 / Loss 21 / Flat 16) / skip 67件
- 成長率目線: 平均log +0.001094 / 幾何平均 +0.109% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DOGS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $106.55

## 4. Latest Market Context

- 更新: 2026-05-07T04:27:34.444823+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=80892.4
- Funnel: target 769 → liquid 186 → pre 50 → checked 50 → surge 6 → strict 1
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.3 >= 65=1, 4h RSI 77.6 >= 65=1, 4h RSI 83.4 >= 65=1, 4h RSI 80.4 >= 65=1, 4h RSI 84.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +250.30% | $1,565,980.92 |
| B3/USDT:USDT | +112.43% | $8,468,304.01 |
| DOGS/USDT:USDT | +81.84% | $10,545,216.81 |
| PENGUIN/USDT:USDT | +58.05% | $1,260,759.03 |
| FHE/USDT:USDT | +40.93% | $16,387,454.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +4.51% | +4.39% |
| AR/USDT:USDT | below_1h_threshold | +4.30% | +4.18% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.81% | +2.69% |
| GALA/USDT:USDT | below_1h_threshold | +2.69% | +2.57% |
| STX/USDT:USDT | below_1h_threshold | +2.56% | +2.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
