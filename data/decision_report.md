# Decision Report

- generated_at: 2026-05-07T14:07:35.865646+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3636**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3636, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.15% | **-0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_9PCT | 4/20 | 20.0% | +7.15% | **+1.43%** |
| LIMIT_8PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT | 7/20 | 35.0% | +3.09% | **+1.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +4.88% | **+3.17%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +4.50% | **+2.93%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +6.18% | **+2.78%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +4.54% | **+2.72%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +3.14% | **+2.35%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$112.33** / 初期 $100.00 (+12.33%)
- 確定: 130件 (Win 44 / Loss 48 / Flat 38) / skip 67件
- 成長率目線: 平均log +0.000894 / 幾何平均 +0.089% per trade / maxDD +2.62%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $112.33

## 4. Latest Market Context

- 更新: 2026-05-07T14:07:32.591588+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=80380.1
- Funnel: target 771 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +97.41% | $10,808,156.15 |
| SATO/USDT:USDT | +90.95% | $3,320,707.55 |
| PENGUIN/USDT:USDT | +68.24% | $4,099,681.07 |
| DOGS/USDT:USDT | +49.88% | $17,220,978.39 |
| NIL/USDT:USDT | +44.96% | $3,838,151.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +3.27% | +3.37% |
| BILL/USDT:USDT | below_1h_threshold | +2.06% | +2.16% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +1.87% | +1.97% |
| SIREN/USDT:USDT | below_1h_threshold | +1.28% | +1.38% |
| WLFI/USDT:USDT | below_1h_threshold | +1.25% | +1.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
