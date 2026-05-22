# Decision Report

- generated_at: 2026-05-22T19:54:17.174515+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4737**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4737, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.88% | **-0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +4.29% | **+1.29%** |
| LIMIT_10PCT | 4/20 | 20.0% | +3.73% | **+0.75%** |
| LIMIT_8PCT | 7/20 | 35.0% | +2.12% | **+0.74%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.29% | **+0.64%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.98% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.94% | **+1.47%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.46% | **+1.38%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.25% | **+1.13%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.95% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$96.20** / 初期 $100.00 (-3.80%)
- 確定トレード: 61件 (TP 16 / SL 42 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $96.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.06** / 初期 $100.00 (+25.06%)
- 確定: 583件 (Win 149 / Loss 188 / Flat 246) / skip 715件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BUILDONBOB/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $125.06

## 4. Latest Market Context

- 更新: 2026-05-22T19:54:10.283680+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.89% price=75818.7
- Funnel: target 765 → liquid 139 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +68.56% | $37,170,963.91 |
| BILL/USDT:USDT | +16.11% | $14,934,969.39 |
| BEAT/USDT:USDT | +10.82% | $37,221,324.80 |
| LAB/USDT:USDT | +5.52% | $28,778,884.12 |
| GENIUS/USDT:USDT | +2.19% | $6,672,641.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +3.88% | +4.77% |
| BSB/USDT:USDT | below_1h_threshold | +3.50% | +4.39% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.98% | +2.87% |
| AGT/USDT:USDT | below_1h_threshold | +1.26% | +2.15% |
| BUILDONBOB/USDT:USDT | below_1h_threshold | +1.00% | +1.89% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
