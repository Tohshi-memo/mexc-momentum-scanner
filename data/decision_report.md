# Decision Report

- generated_at: 2026-05-31T22:20:00.884264+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5232**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5232, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.32% | **-1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.38% | **+0.71%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.89% | **+0.53%** |
| LIMIT_ATR | 18/20 | 90.0% | +0.20% | **+0.18%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.24% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.35% | **+2.01%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.82% | **+1.91%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.45% | **+1.72%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.68% | **+1.52%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.81** / 初期 $100.00 (+34.81%)
- 確定: 867件 (Win 203 / Loss 257 / Flat 407) / skip 926件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $134.81

## 4. Latest Market Context

- 更新: 2026-05-31T22:19:58.069558+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=73875.6
- Funnel: target 773 → liquid 129 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +76.21% | $14,785,593.15 |
| STG/USDT:USDT | +38.41% | $18,996,625.79 |
| HOME/USDT:USDT | +13.72% | $3,017,362.57 |
| ZORA/USDT:USDT | +11.39% | $1,589,466.21 |
| BIANRENSHENG/USDT:USDT | +10.89% | $3,126,303.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +1.82% | +1.80% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.13% | +1.11% |
| LDO/USDT:USDT | below_1h_threshold | +1.11% | +1.09% |
| XLM/USDT:USDT | below_1h_threshold | +1.07% | +1.05% |
| H/USDT:USDT | below_1h_threshold | +1.03% | +1.01% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
