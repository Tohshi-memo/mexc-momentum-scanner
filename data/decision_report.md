# Decision Report

- generated_at: 2026-07-25T19:11:26.201194+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9538**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9538, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.49% | **-0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.35% | **+0.07%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 9/20 | 45.0% | -0.09% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.19% | **+0.95%** |
| MARKET_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.14% | **+0.57%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.71% | **+0.42%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.89% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$454.82** / 初期 $100.00 (+354.82%)
- 確定: 3366件 (Win 1068 / Loss 1090 / Flat 1208) / skip 2733件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $454.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.40** / 初期 $100.00 (+37.40%)
- 確定: 1191件 (Win 328 / Loss 260 / Flat 603) / skip 1758件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1441 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $137.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.96** / 初期 $100.00 (+7.96%)
- 確定: 583件 (Win 197 / Loss 223 / Flat 163) / pending 4件 / skip 423件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000506 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $107.96

## 6. Latest Market Context

- 更新: 2026-07-25T19:11:18.683126+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64399.6
- Funnel: target 898 → liquid 131 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +23.54% | $23,647,260.11 |
| BANK/USDT:USDT | +12.75% | $90,400,207.14 |
| EUL/USDT:USDT | +11.15% | $15,722,295.70 |
| ZAMA/USDT:USDT | +9.02% | $6,960,823.94 |
| ALLO/USDT:USDT | +8.00% | $16,909,456.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +4.24% | +4.21% |
| ZAMA/USDT:USDT | below_1h_threshold | +4.10% | +4.07% |
| ACE/USDT:USDT | below_1h_threshold | +0.54% | +0.52% |
| 1000BONK/USDT:USDT | below_1h_threshold | +0.45% | +0.43% |
| ORDI/USDT:USDT | below_1h_threshold | +0.31% | +0.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
