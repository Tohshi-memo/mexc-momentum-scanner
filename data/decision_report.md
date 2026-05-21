# Decision Report

- generated_at: 2026-05-21T01:58:53.327933+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4593**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4593, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.42% | **+0.50%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +4.25% | **+2.34%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.50% | **+1.37%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.70% | **+1.08%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.49% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 545件 (Win 138 / Loss 185 / Flat 222) / skip 609件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T01:58:48.274108+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=77834.3
- Funnel: target 763 → liquid 129 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +63.23% | $1,143,596.90 |
| EDEN/USDT:USDT | +40.84% | $28,920,917.71 |
| BSB/USDT:USDT | +23.68% | $59,955,889.08 |
| NIL/USDT:USDT | +18.84% | $3,383,342.24 |
| JTO/USDT:USDT | +16.21% | $3,041,098.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_1h_threshold | +4.26% | +4.39% |
| FIGHT/USDT:USDT | below_1h_threshold | +4.19% | +4.32% |
| ONDO/USDT:USDT | below_1h_threshold | +3.75% | +3.87% |
| BANANAS31/USDT:USDT | below_1h_threshold | +3.38% | +3.50% |
| SAHARA/USDT:USDT | below_1h_threshold | +3.04% | +3.17% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
