# Decision Report

- generated_at: 2026-05-25T13:38:33.257169+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4859**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4859, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-3.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.06% | **-3.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 5/20 | 25.0% | +1.01% | **+0.25%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.87% | **+0.17%** |
| LIMIT_8PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |
| LIMIT_10PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |
| LIMIT_9PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +6.33% | **+5.27%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +5.40% | **+3.51%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +5.80% | **+2.90%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +4.68% | **+2.81%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +5.35% | **+1.87%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.19** / 初期 $100.00 (+31.19%)
- 確定: 665件 (Win 169 / Loss 208 / Flat 288) / skip 755件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $131.19

## 4. Latest Market Context

- 更新: 2026-05-25T13:38:29.344551+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=77263.4
- Funnel: target 764 → liquid 121 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +55.15% | $13,131,313.69 |
| SAGA/USDT:USDT | +37.06% | $3,845,231.32 |
| PHA/USDT:USDT | +30.72% | $1,881,966.87 |
| XAN/USDT:USDT | +27.22% | $7,484,960.92 |
| IN/USDT:USDT | +19.48% | $1,078,484.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +2.97% | +3.05% |
| INJ/USDT:USDT | below_1h_threshold | +2.84% | +2.92% |
| NEAR/USDT:USDT | below_1h_threshold | +1.81% | +1.89% |
| RENDER/USDT:USDT | below_1h_threshold | +1.64% | +1.72% |
| H/USDT:USDT | below_1h_threshold | +1.62% | +1.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
