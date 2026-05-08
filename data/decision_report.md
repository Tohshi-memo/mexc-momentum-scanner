# Decision Report

- generated_at: 2026-05-08T00:37:38.983362+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3715**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3715, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 7/20 | 35.0% | +2.03% | **+0.71%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.61% | **+0.46%** |
| LIMIT_BB3S | 3/19 | 15.8% | +1.73% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.56% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.36% | **+0.68%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 23件 (TP 6 / SL 15 / EXP 2)
- 最新: D/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.32
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 189件 (Win 48 / Loss 64 / Flat 77) / skip 87件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T00:37:36.332138+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=79942.9
- Funnel: target 767 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +23.02% | $6,074,445.73 |
| SATO/USDT:USDT | +20.66% | $8,512,598.78 |
| NOT/USDT:USDT | +18.74% | $10,761,563.54 |
| LAB/USDT:USDT | +18.19% | $220,284,823.92 |
| NIL/USDT:USDT | +16.49% | $29,840,943.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.11% | +4.14% |
| NOT/USDT:USDT | below_1h_threshold | +4.03% | +4.07% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.56% | +3.59% |
| D/USDT:USDT | below_1h_threshold | +3.42% | +3.46% |
| BASED/USDT:USDT | below_1h_threshold | +2.63% | +2.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
