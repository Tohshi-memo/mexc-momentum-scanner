# Decision Report

- generated_at: 2026-05-31T15:16:14.446631+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5196**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5196, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.08% | **-1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.75% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.16% | **+1.73%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.97% | **+1.48%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.40% | **+1.33%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.23% | **+0.78%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.40** / 初期 $100.00 (+26.40%)
- 確定: 831件 (Win 191 / Loss 248 / Flat 392) / skip 926件
- 成長率目線: 平均log +0.000282 / 幾何平均 +0.028% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $126.40

## 4. Latest Market Context

- 更新: 2026-05-31T15:16:11.807015+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=73635.5
- Funnel: target 773 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +54.11% | $10,624,998.92 |
| AIA/USDT:USDT | +51.05% | $4,679,271.75 |
| STG/USDT:USDT | +28.47% | $4,677,835.57 |
| BIANRENSHENG/USDT:USDT | +24.55% | $1,998,743.33 |
| PORTAL/USDT:USDT | +23.92% | $9,611,754.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +4.93% | +4.84% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +2.88% | +2.79% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.50% | +2.41% |
| UP/USDT:USDT | below_1h_threshold | +1.72% | +1.63% |
| STG/USDT:USDT | below_1h_threshold | +1.32% | +1.23% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
