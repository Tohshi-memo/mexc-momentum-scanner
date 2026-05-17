# Decision Report

- generated_at: 2026-05-17T15:13:46.169461+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4408**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4408, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.08% | **-1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.73% | **+0.17%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.19% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.87% | **+1.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.28% | **+1.28%** |
| MARKET_LONG | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.29% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 405件 (Win 104 / Loss 137 / Flat 164) / skip 564件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $119.41

## 4. Latest Market Context

- 更新: 2026-05-17T15:13:43.914182+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=78056.3
- Funnel: target 760 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +65.97% | $2,541,616.25 |
| BSB/USDT:USDT | +46.80% | $17,293,154.34 |
| AIA/USDT:USDT | +42.23% | $19,321,831.51 |
| FHE/USDT:USDT | +19.20% | $2,724,672.40 |
| CGPT/USDT:USDT | +17.66% | $2,412,050.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.18% | +3.12% |
| FHE/USDT:USDT | below_1h_threshold | +2.54% | +2.48% |
| APE/USDT:USDT | below_1h_threshold | +1.51% | +1.45% |
| HYPE/USDT:USDT | below_1h_threshold | +1.17% | +1.11% |
| CGPT/USDT:USDT | below_1h_threshold | +0.69% | +0.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
