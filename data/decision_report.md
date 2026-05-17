# Decision Report

- generated_at: 2026-05-17T08:43:27.845384+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4394**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4394, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.50% | **-0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 5/20 | 25.0% | +2.35% | **+0.59%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.26% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.66% | **+1.08%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.33% | **+1.06%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.63% | **+1.06%** |
| ASK_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |
| MARKET_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.82** / 初期 $100.00 (+17.82%)
- 確定: 394件 (Win 98 / Loss 137 / Flat 159) / skip 561件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $117.82

## 4. Latest Market Context

- 更新: 2026-05-17T08:43:22.024953+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=78017.1
- Funnel: target 760 → liquid 119 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +30.22% | $10,650,512.84 |
| CGPT/USDT:USDT | +21.41% | $2,098,503.22 |
| BSB/USDT:USDT | +19.07% | $5,074,729.48 |
| ASTEROID/USDT:USDT | +17.31% | $4,390,485.25 |
| AIGENSYN/USDT:USDT | +12.38% | $2,636,330.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +3.15% | +3.30% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.80% | +2.95% |
| AIA/USDT:USDT | below_1h_threshold | +2.11% | +2.26% |
| NMR/USDT:USDT | below_1h_threshold | +1.84% | +1.99% |
| KAIA/USDT:USDT | below_1h_threshold | +1.14% | +1.29% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
