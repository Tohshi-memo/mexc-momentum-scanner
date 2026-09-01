# Decision Report

- generated_at: 2026-09-01T19:21:28.384939+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13261**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13261, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.47% | **+1.11%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.96% | **+0.99%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.00% | **+0.90%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.15% | **+2.15%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.58% | **+1.26%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +3.03% | **+0.91%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.20% | **+0.77%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$804.58** / 初期 $100.00 (+704.58%)
- 確定: 4896件 (Win 1490 / Loss 1614 / Flat 1792) / skip 4926件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $804.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.03** / 初期 $100.00 (+75.03%)
- 確定: 2240件 (Win 626 / Loss 539 / Flat 1075) / skip 4432件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0873 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $175.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.08** / 初期 $100.00 (+15.08%)
- 確定: 2088件 (Win 610 / Loss 816 / Flat 662) / pending 1件 / skip 2645件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000198 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.08

## 6. Latest Market Context

- 更新: 2026-09-01T19:21:13.105824+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=77210.4
- Funnel: target 1036 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +15.05% | $1,072,138.38 |
| USELESS/USDT:USDT | +13.22% | $35,666,271.18 |
| ACE/USDT:USDT | +12.51% | $5,528,231.11 |
| MAGMA/USDT:USDT | +10.68% | $1,925,515.78 |
| FILECOIN/USDT:USDT | +9.94% | $11,317,059.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +2.20% | +2.08% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.10% | +1.98% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.89% | +1.77% |
| BEAT/USDT:USDT | below_1h_threshold | +1.78% | +1.66% |
| ZORA/USDT:USDT | below_1h_threshold | +1.47% | +1.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
