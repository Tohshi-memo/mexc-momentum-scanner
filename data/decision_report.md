# Decision Report

- generated_at: 2026-05-17T14:49:01.623438+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4405**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4405, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.48% | **-0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.82% | **+0.57%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.38% | **+0.30%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.45% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.17% | **+1.63%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.50% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +1.26% | **+0.84%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.23% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 402件 (Win 104 / Loss 137 / Flat 161) / skip 564件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.75% 残高後 $119.41

## 4. Latest Market Context

- 更新: 2026-05-17T14:48:56.065623+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=78013.6
- Funnel: target 760 → liquid 122 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.9 >= 65=1, 4h RSI 77.1 >= 65=1, 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +65.97% | $1,735,125.57 |
| BSB/USDT:USDT | +51.59% | $16,674,188.33 |
| AIA/USDT:USDT | +43.72% | $17,830,153.59 |
| CGPT/USDT:USDT | +17.08% | $2,435,040.96 |
| KAIA/USDT:USDT | +16.72% | $3,228,018.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RUNE/USDT:USDT | below_1h_threshold | +2.73% | +2.92% |
| DUSK/USDT:USDT | below_1h_threshold | +2.52% | +2.72% |
| APE/USDT:USDT | below_1h_threshold | +2.46% | +2.66% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.17% | +2.36% |
| GUA/USDT:USDT | below_1h_threshold | +1.67% | +1.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
