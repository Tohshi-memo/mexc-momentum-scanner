# Decision Report

- generated_at: 2026-05-14T20:16:38.552109+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4309**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4309, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +6.29% | **+1.26%** |
| LIMIT_8PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_BB3S | 5/13 | 38.5% | +2.96% | **+1.14%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +1.14% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.64% | **+1.64%** |
| ASK_LONG | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +2.08% | **+0.89%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.41% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.48** / 初期 $100.00 (+20.48%)
- 確定: 363件 (Win 96 / Loss 129 / Flat 138) / skip 507件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CRCLSTOCK/USDT:USDT `LIMIT_BB3S` TP_HIT account +1.00% 残高後 $120.48

## 4. Latest Market Context

- 更新: 2026-05-14T20:16:35.083475+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=81361.4
- Funnel: target 759 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UP/USDT:USDT | +16.38% | $2,921,123.05 |
| NAORIS/USDT:USDT | +10.25% | $2,879,329.34 |
| LAB/USDT:USDT | +9.53% | $121,792,588.54 |
| FIGSTOCK/USDT:USDT | +8.10% | $1,557,826.32 |
| TROLLSOL/USDT:USDT | +7.69% | $1,775,717.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +3.68% | +3.70% |
| AMATSTOCK/USDT:USDT | below_1h_threshold | +3.67% | +3.68% |
| LAB/USDT:USDT | below_1h_threshold | +1.73% | +1.74% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.61% | +1.62% |
| COLLECT/USDT:USDT | below_1h_threshold | +0.93% | +0.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
