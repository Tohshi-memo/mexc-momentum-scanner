# Decision Report

- generated_at: 2026-05-20T09:54:00.170792+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4537**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4537, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.82% | **-0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 13/20 | 65.0% | +0.73% | **+0.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.54% | **+0.19%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.14% | **-0.11%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |
| LIMIT_7PCT | 3/20 | 15.0% | -1.73% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.59%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.44% | **+0.29%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +0.38% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.27** / 初期 $100.00 (+26.27%)
- 確定: 499件 (Win 131 / Loss 170 / Flat 198) / skip 599件
- 成長率目線: 平均log +0.000467 / 幾何平均 +0.047% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $126.27

## 4. Latest Market Context

- 更新: 2026-05-20T09:53:51.764698+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77465.1
- Funnel: target 762 → liquid 133 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +103.46% | $1,567,829.95 |
| PROMPT/USDT:USDT | +31.65% | $12,543,616.93 |
| FIDA/USDT:USDT | +28.49% | $2,821,902.11 |
| EDEN/USDT:USDT | +27.29% | $22,073,823.41 |
| PLAY/USDT:USDT | +23.21% | $10,434,834.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROMPT/USDT:USDT | below_1h_threshold | +3.24% | +3.19% |
| EDEN/USDT:USDT | below_1h_threshold | +3.19% | +3.14% |
| DASH/USDT:USDT | below_1h_threshold | +1.88% | +1.83% |
| VVV/USDT:USDT | below_1h_threshold | +1.81% | +1.76% |
| FOGO/USDT:USDT | below_1h_threshold | +1.57% | +1.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
