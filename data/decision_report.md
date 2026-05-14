# Decision Report

- generated_at: 2026-05-14T11:13:15.873437+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4284**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4284, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.18% | **+0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/12 | 41.7% | +4.85% | **+2.02%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.48% | **+1.19%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.27% | **+1.02%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +3.24% | **+2.32%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.19% | **+1.28%** |
| MARKET_LONG | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.66% | **+0.58%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$96.73** / 初期 $100.00 (-3.27%)
- 確定トレード: 42件 (TP 10 / SL 29 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.73
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 344件 (Win 94 / Loss 125 / Flat 125) / skip 501件
- 成長率目線: 平均log +0.000510 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T11:13:12.501220+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=79519.0
- Funnel: target 763 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +60.01% | $4,996,038.69 |
| TROLLSOL/USDT:USDT | +29.77% | $2,211,724.40 |
| UP/USDT:USDT | +28.67% | $1,766,675.91 |
| STAR/USDT:USDT | +21.71% | $2,071,472.33 |
| CSCOSTOCK/USDT:USDT | +18.91% | $5,508,150.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STAR/USDT:USDT | below_1h_threshold | +3.28% | +3.30% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.10% | +2.11% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +0.66% | +0.67% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +0.64% | +0.65% |
| BEAT/USDT:USDT | below_1h_threshold | +0.43% | +0.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
