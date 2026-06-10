# Decision Report

- generated_at: 2026-06-10T08:23:56.251583+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6202**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6202, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.31% | **+0.14%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.95% | **+1.95%** |
| ASK_LONG | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_ATR_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +0.77% | **+0.46%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +0.92% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.03** / 初期 $100.00 (+52.03%)
- 確定: 1218件 (Win 303 / Loss 377 / Flat 538) / skip 1545件
- 成長率目線: 平均log +0.000344 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $152.03

## 4. Latest Market Context

- 更新: 2026-06-10T08:23:53.557396+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=61551.5
- Funnel: target 785 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +49.65% | $8,405,928.94 |
| BTW/USDT:USDT | +28.08% | $30,019,088.35 |
| KAT/USDT:USDT | +22.47% | $1,001,197.98 |
| ESPORTS/USDT:USDT | +21.36% | $24,500,253.76 |
| UB/USDT:USDT | +19.78% | $2,157,855.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.30% | +4.47% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.07% | +2.24% |
| BLESS/USDT:USDT | below_1h_threshold | +2.00% | +2.17% |
| RUNE/USDT:USDT | below_1h_threshold | +1.93% | +2.09% |
| UB/USDT:USDT | below_1h_threshold | +1.57% | +1.74% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
