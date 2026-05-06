# Decision Report

- generated_at: 2026-05-06T21:42:37.759580+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3503**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3503, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.98% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.01% | **+0.01%** |
| LIMIT_BB3S | 4/12 | 33.3% | -0.65% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +4.62% | **+2.31%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.20% | **+1.98%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.32% | **+1.74%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.67% | **+1.08%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.35% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 55件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T21:42:34.235232+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=81528.8
- Funnel: target 764 → liquid 192 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.3 >= 65=1, 4h RSI 79.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +52.77% | $13,299,275.13 |
| BILL/USDT:USDT | +15.70% | $7,794,918.50 |
| ZEREBRO/USDT:USDT | +11.43% | $1,408,649.58 |
| LAB/USDT:USDT | +9.94% | $242,096,083.41 |
| DOGS/USDT:USDT | +8.28% | $6,420,907.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OP/USDT:USDT | below_1h_threshold | +4.55% | +4.36% |
| ICP/USDT:USDT | below_1h_threshold | +3.94% | +3.75% |
| SIREN/USDT:USDT | below_1h_threshold | +3.46% | +3.27% |
| LAB/USDT:USDT | below_1h_threshold | +3.41% | +3.23% |
| BRETT/USDT:USDT | below_1h_threshold | +3.10% | +2.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
