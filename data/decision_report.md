# Decision Report

- generated_at: 2026-05-06T12:05:07.709613+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3451**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3451, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/14 | 28.6% | +0.46% | **+0.13%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.00% | **-0.00%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.04% | **-0.00%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.06% | **-0.03%** |
| LIMIT_6PCT | 2/20 | 10.0% | -0.49% | **-0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.76% | **+1.24%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.85% | **+1.20%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.89% | **+0.94%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.63% | **+0.90%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.08% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 3件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T12:05:05.079964+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=82355.9
- Funnel: target 770 → liquid 198 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BILL/USDT:USDT | +47.09% | $3,602,361.48 |
| B3/USDT:USDT | +42.53% | $1,533,486.71 |
| IO/USDT:USDT | +38.77% | $13,537,327.07 |
| FHE/USDT:USDT | +37.74% | $30,003,437.59 |
| ZEC/USDT:USDT | +33.57% | $759,594,200.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +1.21% | +1.36% |
| LAB/USDT:USDT | below_1h_threshold | +1.13% | +1.29% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.77% | +0.93% |
| GALA/USDT:USDT | below_1h_threshold | +0.57% | +0.72% |
| OP/USDT:USDT | below_1h_threshold | +0.52% | +0.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
