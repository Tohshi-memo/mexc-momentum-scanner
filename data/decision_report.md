# Decision Report

- generated_at: 2026-05-09T13:51:42.410872+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3884**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3884, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_BB3S | 4/12 | 33.3% | +0.34% | **+0.11%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| ASK | 20/20 | 100.0% | +0.06% | **+0.06%** |
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +1.22% | **+0.92%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.89% | **+0.44%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.81% | **+0.32%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.57% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 194件 (Win 48 / Loss 64 / Flat 82) / skip 251件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T13:51:39.360389+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=80312.0
- Funnel: target 769 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYM/USDT:USDT | +35.97% | $6,155,008.89 |
| ZEREBRO/USDT:USDT | +32.97% | $3,269,095.50 |
| PLAY/USDT:USDT | +25.85% | $25,694,990.75 |
| SAHARA/USDT:USDT | +23.76% | $3,747,092.90 |
| BILL/USDT:USDT | +22.90% | $20,015,780.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +4.06% | +4.12% |
| LIT/USDT:USDT | below_1h_threshold | +2.96% | +3.02% |
| BILL/USDT:USDT | below_1h_threshold | +2.42% | +2.49% |
| AERO/USDT:USDT | below_1h_threshold | +1.92% | +1.99% |
| DYM/USDT:USDT | below_1h_threshold | +1.67% | +1.74% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
