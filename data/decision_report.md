# Decision Report

- generated_at: 2026-05-31T16:55:34.272142+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5207**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5207, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.08% | **-1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.57% | **+0.43%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.27% | **+0.23%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +4.00% | **+2.40%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.69% | **+1.48%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.26% | **+1.13%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.54% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.97** / 初期 $100.00 (+27.97%)
- 確定: 842件 (Win 194 / Loss 251 / Flat 397) / skip 926件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $127.97

## 4. Latest Market Context

- 更新: 2026-05-31T16:55:31.426606+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=73504.5
- Funnel: target 773 → liquid 125 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.3 >= 65=1, 4h RSI 83.7 >= 65=1, 4h RSI 84.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +9.55% | $10,334,176.07 |
| AIA/USDT:USDT | +5.85% | $5,509,731.48 |
| STG/USDT:USDT | +5.24% | $5,510,917.70 |
| HOME/USDT:USDT | +3.92% | $1,713,344.76 |
| RAVE/USDT:USDT | +3.00% | $1,752,475.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.92% | +4.07% |
| RAVE/USDT:USDT | below_1h_threshold | +3.00% | +3.15% |
| ALLO/USDT:USDT | below_1h_threshold | +2.62% | +2.76% |
| WLD/USDT:USDT | below_1h_threshold | +1.79% | +1.94% |
| HIVE/USDT:USDT | below_1h_threshold | +1.63% | +1.77% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
