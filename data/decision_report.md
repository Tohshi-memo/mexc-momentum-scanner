# Decision Report

- generated_at: 2026-07-25T18:01:16.539723+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9535**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9535, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.49% | **-0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/17 | 17.6% | +0.77% | **+0.14%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.31% | **-0.06%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.33% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.38% | **+1.10%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.41% | **+0.92%** |
| MARKET_LONG | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +0.56% | **+0.22%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +0.47% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$446.31** / 初期 $100.00 (+346.31%)
- 確定: 3363件 (Win 1065 / Loss 1090 / Flat 1208) / skip 2733件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $446.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$135.65** / 初期 $100.00 (+35.65%)
- 確定: 1188件 (Win 325 / Loss 260 / Flat 603) / skip 1758件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1421 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $135.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.40** / 初期 $100.00 (+7.40%)
- 確定: 580件 (Win 195 / Loss 223 / Flat 162) / pending 6件 / skip 422件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000464 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $107.40

## 6. Latest Market Context

- 更新: 2026-07-25T18:01:09.793512+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64250.5
- Funnel: target 898 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +15.10% | $90,090,196.95 |
| ESPORTS/USDT:USDT | +12.03% | $21,805,023.89 |
| DEXE/USDT:USDT | +6.85% | $127,645,819.38 |
| ZAMA/USDT:USDT | +6.27% | $6,742,606.12 |
| SHIB/USDT:USDT | +6.25% | $16,645,545.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +1.18% | +1.15% |
| KORU/USDT:USDT | below_1h_threshold | +0.70% | +0.68% |
| EUL/USDT:USDT | below_1h_threshold | +0.65% | +0.63% |
| SHIB/USDT:USDT | below_1h_threshold | +0.58% | +0.56% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +0.46% | +0.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
