# Decision Report

- generated_at: 2026-05-08T09:17:28.262173+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3761**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.34% / filled 20/20。**
- 全期間 MARKET基準: n=3761, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.48% | **+1.48%** |
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.32% | **+1.25%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.82% | **+0.37%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.30% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.07% | **-0.05%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | -0.14% | **-0.08%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.36% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 26件 (TP 7 / SL 17 / EXP 2)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 190件 (Win 48 / Loss 64 / Flat 78) / skip 132件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T09:17:25.225743+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=79919.9
- Funnel: target 771 → liquid 181 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +38.74% | $7,022,145.75 |
| PLAY/USDT:USDT | +24.73% | $8,240,832.02 |
| STRK/USDT:USDT | +24.57% | $13,881,663.13 |
| SATO/USDT:USDT | +23.80% | $9,180,394.37 |
| AGT/USDT:USDT | +23.64% | $5,217,004.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRK/USDT:USDT | below_1h_threshold | +2.56% | +2.47% |
| BSB/USDT:USDT | below_1h_threshold | +2.32% | +2.24% |
| ARKM/USDT:USDT | below_1h_threshold | +2.21% | +2.12% |
| ARB/USDT:USDT | below_1h_threshold | +1.88% | +1.79% |
| W/USDT:USDT | below_1h_threshold | +1.71% | +1.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
