# Decision Report

- generated_at: 2026-05-10T22:52:53.566376+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3996**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.70% / filled 20/20。**
- 全期間 MARKET基準: n=3996, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.85% | **+0.86%** |
| ASK | 20/20 | 100.0% | +0.70% | **+0.70%** |
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.64% | **+0.61%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +2.24% | **+1.91%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +0.99% | **+0.85%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.07% | **+0.80%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.28% | **+0.77%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.60% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$109.48** / 初期 $100.00 (+9.48%)
- 確定: 204件 (Win 51 / Loss 68 / Flat 85) / skip 353件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $109.48

## 4. Latest Market Context

- 更新: 2026-05-10T22:52:50.082599+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.51% price=81895.5
- Funnel: target 769 → liquid 178 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.4 >= 65=1, 4h RSI 90.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +62.39% | $6,454,018.09 |
| TROLLSOL/USDT:USDT | +25.50% | $4,745,350.70 |
| ALCH/USDT:USDT | +22.27% | $3,512,977.38 |
| B/USDT:USDT | +15.00% | $2,467,571.27 |
| SAHARA/USDT:USDT | +10.20% | $2,025,309.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAHARA/USDT:USDT | below_1h_threshold | +4.88% | +3.37% |
| NIL/USDT:USDT | below_1h_threshold | +4.29% | +2.78% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +4.00% | +2.48% |
| IP/USDT:USDT | below_1h_threshold | +3.74% | +2.23% |
| JUP/USDT:USDT | below_1h_threshold | +3.64% | +2.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
